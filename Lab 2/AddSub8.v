`timescale 1ns / 1ps

module AddSub8(
    input [7:0] A,
    input [7:0] B,
    input sub, // Subtract control signal
    output [7:0] S,
    output ovfl
);
    wire [7:0] B_inv;    // Inverted B for subtraction
    wire carry_out;      // Carry out from the adder
    wire carry_in = sub; // Carry in is set to 1 for subtraction
    
    // this might be wrong, please remember 2 complements
    assign B_inv = (B & ~{8{sub}}) | (~B & {8{sub}});

    // Use Add8 module for addition/subtraction
    Add8 adder(
        .A(A),
        .B(B_inv),
        .Cin(carry_in),
        .S(S),
        .Cout(carry_out),
        .ovfl(ovfl)
    );
endmodule
