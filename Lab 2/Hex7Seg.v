`timescale 1ns / 1ps

module Hex7Seg(
    input [3:0] n,  // 4-bit input
    output [6:0] seg // 7-bit output for 7-segment display
);
    // Segment A (CA)
    assign seg[0] = ~((n[1] & n[2]) | (n[1] & ~n[3]) | (n[3] & ~n[0]) | (~n[0] & ~n[2]) | (n[0] & n[2] & ~n[3]) | (n[3] & ~n[1] & ~n[2]));
    // Segment B (CB)
    assign seg[1] = ~((~n[0] & ~n[2]) | (~n[1] & ~n[2]) | (n[0] & n[1] & ~n[3]) | (n[0] & n[3] & ~n[1]) | (~n[0] & ~n[1] & ~n[3]));
    // Segment C (CC)
    assign seg[2] = ~((n[0] & ~n[1]) | (n[0] & ~n[2]) | (n[2] & ~n[3]) | (n[3] & ~n[2]) | (~n[1] & ~n[2]));
    // Segment D (CD)
    assign seg[3] = ~((n[3] & ~n[1]) | (n[0] & n[1] & ~n[2]) | (n[0] & n[2] & ~n[1]) | (n[1] & n[2] & ~n[0]) | (~n[0] & ~n[2] & ~n[3]));
    // Segment E (CE)
    assign seg[4] = ~((n[1] & n[3]) | (n[2] & n[3]) | (n[1] & ~n[0]) | (~n[0] & ~n[2]));
    // Segment F (CF)
    assign seg[5] = ~((n[1] & n[3]) | (n[2] & ~n[0]) | (n[3] & ~n[2]) | (~n[0] & ~n[1]) | (n[2] & ~n[1] & ~n[3]));
    // Segment G (CG)
    assign seg[6] = ~((n[0] & n[3]) | (n[1] & ~n[0]) | (n[1] & ~n[2]) | (n[3] & ~n[2]) | (n[2] & ~n[1] & ~n[3]));
endmodule