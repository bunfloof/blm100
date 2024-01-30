`timescale 1ns / 1ps

module countUD5L(
    input clk,
    input UD,
    input CE,
    input LD,
    input [4:0] Din,
    output [4:0] Q,
    output UTC,
    output DTC
);

wire [4:0] count_up;
wire [4:0] count_down;
wire [4:0] next_state;

// Logicfor counting up and down (DO NOT UNCOMMENT)
// This is fine for now, but in final submission, do not use + or - 
//assign count_up = Q + 1;
//assign count_down = Q - 1;

// counting up
assign count_up[0] = Q[0] ^ CE;
assign count_up[1] = Q[1] ^ (CE & Q[0]);
assign count_up[2] = Q[2] ^ (CE & Q[0] & Q[1]);
assign count_up[3] = Q[3] ^ (CE & Q[0] & Q[1] & Q[2]);
assign count_up[4] = Q[4] ^ (CE & Q[0] & Q[1] & Q[2] & Q[3]);

// counting down (maybe fixed)?
assign count_down[0] = Q[0] ^ CE;
assign count_down[1] = Q[1] ^ (CE & ~Q[0]);
assign count_down[2] = Q[2] ^ (CE & ~Q[0] & ~Q[1]);
assign count_down[3] = Q[3] ^ (CE & ~Q[0] & ~Q[1] & ~Q[2]);
assign count_down[4] = Q[4] ^ (CE & ~Q[0] & ~Q[1] & ~Q[2] & ~Q[3]);

// Next state logic
assign next_state[0] = (LD & Din[0]) | (~LD & ((UD & count_up[0]) | (~UD & count_down[0])));
assign next_state[1] = (LD & Din[1]) | (~LD & ((UD & count_up[1]) | (~UD & count_down[1])));
assign next_state[2] = (LD & Din[2]) | (~LD & ((UD & count_up[2]) | (~UD & count_down[2])));
assign next_state[3] = (LD & Din[3]) | (~LD & ((UD & count_up[3]) | (~UD & count_down[3])));
assign next_state[4] = (LD & Din[4]) | (~LD & ((UD & count_up[4]) | (~UD & count_down[4])));

// Instantiate FDRE flip-flops for each bit of the counter
FDRE #(.INIT(1'b0)) ff0 (.C(clk), .CE(CE | LD), .R(1'b0), .D(next_state[0]), .Q(Q[0]));
FDRE #(.INIT(1'b0)) ff1 (.C(clk), .CE(CE | LD), .R(1'b0), .D(next_state[1]), .Q(Q[1]));
FDRE #(.INIT(1'b0)) ff2 (.C(clk), .CE(CE | LD), .R(1'b0), .D(next_state[2]), .Q(Q[2]));
FDRE #(.INIT(1'b0)) ff3 (.C(clk), .CE(CE | LD), .R(1'b0), .D(next_state[3]), .Q(Q[3]));
FDRE #(.INIT(1'b0)) ff4 (.C(clk), .CE(CE | LD), .R(1'b0), .D(next_state[4]), .Q(Q[4]));

// UTC and DTC logic
assign UTC = &Q; // UTC when all bits of Q are 1
assign DTC = ~|Q; // DTC when all bits of Q are 0

endmodule
