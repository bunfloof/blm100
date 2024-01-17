`timescale 1ns / 1ps

module Add8(
    input [7:0] A,
    input [7:0] B,
    input Cin,
    output [7:0] S,
    output ovfl,
    output Cout
);
    wire[7:0] carry; // Internal carries between full adders

    // Instantiate Full Adders for each bit
    FullAdder FA0(A[0], B[0], Cin, S[0], carry[0]);
    FullAdder FA1(A[1], B[1], carry[0], S[1], carry[1]);
    FullAdder FA2(A[2], B[2], carry[1], S[2], carry[2]);
    FullAdder FA3(A[3], B[3], carry[2], S[3], carry[3]);
    FullAdder FA4(A[4], B[4], carry[3], S[4], carry[4]);
    FullAdder FA5(A[5], B[5], carry[4], S[5], carry[5]);
    FullAdder FA6(A[6], B[6], carry[5], S[6], carry[6]);
    FullAdder FA7(A[7], B[7], carry[6], S[7], Cout);

    // Overflow occurs when the carry into the last bit is different from the carry out
    assign ovfl = carry[6] ^ Cout;
endmodule