`timescale 1ns / 1ps

module FullAdder(
    input a, b, Cin,
    output s, Cout
);
    assign s = a ^ b ^ Cin;
    assign Cout = (a & b) | (b & Cin) | (a & Cin);
endmodule
