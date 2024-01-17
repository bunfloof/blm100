`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:  Martine
// 
// Create Date: 9/27/2022 09:26:52 PM
// Design Name: 
// Module Name: test_add
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module test_addsub( ); // no inputs/outputs, this is a wrapper


// registers to hold values for the inputs to your top level
    reg [15:0] sw;
    reg btnU, btnR, clkin;
// wires to see the values of the outputs of your top level
    wire [6:0] seg;
    wire [3:0] an;
    wire dp;
    wire [15:0] led;
    
// create one instance of your top level
// and attach it to the registers and wires created above
    AddSubDisplayControl UUT (
     .sw(sw),
     .btnU(btnU),
     .btnR(btnR), 
     .clkin(clkin),
     .seg(seg),
     .an(an),
     .led(led),
     .dp(dp)
    );
    
    
// create an oscillating signal to impersonate the clock provided on the BASYS 3 board
    // Clock simulation
    parameter PERIOD = 10;
    initial begin
        clkin = 0;
        forever #(PERIOD/2) clkin = ~clkin;
    end

    // Test vectors
    initial begin
        // Initialize
        sw = 0; btnU = 0; btnR = 0;

        // Test Vector 1.1: Positive Values, No Overflow (sub=0)
        #500 sw = {8'h40, 8'h3F}; btnU = 0;

        // Test Vector 1.2: Positive Values, Overflow (sub=0)
        #500 sw = {8'h50, 8'h40}; btnU = 0;

        // Test Vector 1.3: Negative Values, No Overflow (sub=0)
        #500 sw = {8'h81, 8'h81}; btnU = 0;

        // Test Vector 1.4: Negative Values, Overflow (sub=0)
        #500 sw = {8'h80, 8'h80}; btnU = 0;

        // Test Vector 1.5: A Positive, B Negative, Result in Overflow (sub=1)
        #500 sw = {8'h7F, 8'h80}; btnU = 1;

        // End simulation
        #500 $finish;
          
    end

endmodule
