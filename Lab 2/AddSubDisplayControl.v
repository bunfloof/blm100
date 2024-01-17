`timescale 1ns / 1ps

module AddSubDisplayControl(
    input [15:0] sw,
    input btnU, btnR, clkin,
    output [6:0] seg,
    output dp,
    output [3:0] an,
    output [15:0] led
);
    wire [7:0] result; // Output of the adder/subtractor
    wire ovfl; // Overflow flag
    wire [3:0] hex_low, hex_high; // Lower and higher nibble of result
    wire [6:0] seg_low, seg_high; // Segments for lower and higher nibble tutor confirmed it's 6:0 for 7 seg display duh 
    wire dig_sel; // Digit select signal for multiplexing display

    // Instantiate AddSub8 module
    AddSub8 addsub(
        .A(sw[15:8]),
        .B(sw[7:0]),
        .sub(btnU),
        .S(result),
        .ovfl(ovfl)
    );

    // Split the result into higher and lower nibbles
    assign hex_low = result[3:0];
    assign hex_high = result[7:4];

    // Instantiate two Hex7Seg modules for each nibble
    Hex7Seg hex_to_seg_low(
        .n(hex_low),
        .seg(seg_low)
    );

    Hex7Seg hex_to_seg_high(
        .n(hex_high),
        .seg(seg_high)
    );

    // Instantiate lab2_digsel for digit selection
    lab2_digsel digsel_inst(
        .clkin(clkin),
        .greset(btnR),
        .digsel(dig_sel)
    );

    // Instantiate Multiplexer2To1_8bit for controlling which digit to display
    // tutor said this might be wrong because if seg_low and seg_high are 7 bits, how does that fit into 8 bits?
    Multiplexer2To1_8bit mux(
        .in0(seg_low),
        .in1(seg_high),
        .sel(dig_sel),
        .out(seg)
    );

    // Anode signals for the 7-segment display control
    // tutor said one of them is ~dig_sel, but I'm not gonna tell you which one.
    assign an[0] = dig_sel;
    assign an[1] = ~dig_sel; // this one is ~dig_sel
    assign an[2] = 1'b1; // Set to high because they're unused
    assign an[3] = 1'b1; // Set to high because they're unused
    
    // Set the decimal point and led outputs
    assign dp = ~ovfl; // Light up the decimal point on overflow
    assign led = sw; // Directly connect switches to LEDs for testing
endmodule
