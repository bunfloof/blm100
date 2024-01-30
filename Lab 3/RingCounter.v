`timescale 1ns / 1ps

module RingCounter(
    input clk,
    input Advance,
    output [3:0] Q // Change the size as per requirement
);

// FDRE instantiatior=n for each stage of the Ring Counter
// I did .R(1'b0) meaning I DISBALED RESET
FDRE #(.INIT(1'b1)) fdre0 (.C(clk), .CE(Advance), .D(Q[3]), .R(1'b0), .Q(Q[0]));

FDRE #(.INIT(1'b0)) fdre1 (.C(clk), .CE(Advance), .D(Q[0]), .R(1'b0), .Q(Q[1]));

FDRE #(.INIT(1'b0)) fdre2 (.C(clk), .CE(Advance), .D(Q[1]), .R(1'b0), .Q(Q[2]));

FDRE #(.INIT(1'b0)) fdre3 (.C(clk), .CE(Advance), .D(Q[2]), .R(1'b0), .Q(Q[3]));

endmodule
