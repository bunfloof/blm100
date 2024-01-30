`timescale 1ns / 1ps

module TopLevelDisplayCounter(
    input clkin,        // 100MHz clock from the BASYS3 Board
    input btnR,         // Reset button connected to the built-in global reset
    input btnU,         // Button to increment or decrement counter
    input btnC,         // Button for continuous advance
    input btnL,         // Load button for counter
    input [15:0] sw,    // Switches input
    output [6:0] seg,   // 7-segment display segments
    output dp,          // 7-segment display decimal point
    output [3:0] an,    // 7-segment display anodes
    output [15:0] led   // LEDs
);

    // Clock management
    wire clk;
    wire digsel;        // Digital selection signal
    
    // The signal clk is your system clock. The signal digsel should be used to advance the Ring Counter; it should not be used as a clock
    // Pushbutton btnR should be connected only to the .greset input of labCnt_clks, no where else!
    labCnt_clks slowit (.clkin(clkin), .greset(btnR), .clk(clk), .digsel(digsel));

    // Edge Detector for btnU
    wire edge_detected;
    EdgeDetector edge_detect (.clk(clk), .signal(btnU), .edge_detected(edge_detected));

    // 15-bit Counter
    wire [14:0] counter_output;
    
    // Continuous advance logic, Should I do btnC &| Q[14:2]? NOT ALLOWED TO USE COMPARISONS
    //wire continuous_advance = btnC & ~((counter_output >= 15'h7FFC) & (counter_output <= 15'h7FFF));
    wire continuous_advance = btnC & ~(&counter_output[14:2]);
    
    wire counter_utc, counter_dtc;
    countUD15L main_counter (
        .clk(clk),
        .UD(sw[0]), // Direction of the count down or up? Is this correct?
        .CE(edge_detected | continuous_advance), // maybe
        .LD(btnL),
        .Din(sw[15:1]),
        .Q(counter_output),
        .UTC(counter_utc),
        .DTC(counter_dtc)
    );

    // Ring Counter for display control
    wire [3:0] ring_output;
    RingCounter display_control (.clk(clk), .Advance(digsel), .Q(ring_output));

    // Selector for choosing display segment
    wire [3:0] display_data;
    Selector display_selector (.N({1'b0,counter_output}), .sel(ring_output), .H(display_data));

    // 7-segment Display Module
    Hex7Seg display (.n(display_data), .seg(seg));

    // LED and other outputs
    assign led[15] = counter_utc; // UTC indicator maybe (counter_output == 15'h7FFF)
    assign led[0] = counter_dtc;  // DTC indicator maybe (counter_output == 0)
    assign led[14:1] = 14'b0;     // Other LEDs OFF
    assign an = ~ring_output;     // Active low corresponding 7-segment display
    assign dp = 1'b1;             // Decimal point off

endmodule
