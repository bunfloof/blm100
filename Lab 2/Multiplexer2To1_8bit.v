`timescale 1ns / 1ps

module Multiplexer2To1_8bit(
    input [6:0] in0, // Input 0 (7-bit)
    input [6:0] in1, // Input 1 (7-bit)
    input sel,       // Selection bit
    output [6:0] out // Output (7-bit)
);
    assign out = (in0 & ~{7{sel}}) | (in1 & {7{sel}});
endmodule
