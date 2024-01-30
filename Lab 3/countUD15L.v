`timescale 1ns / 1ps

module countUD15L(
    input clk,
    input UD,
    input CE,
    input LD,
    input [14:0] Din,
    output [14:0] Q,
    output UTC,
    output DTC
);

// Intermediate signals for UTC and DTC
wire UTC0, UTC1, DTC0, DTC1, UTC2, DTC2;
wire [4:0] Q0, Q1, Q2;

// Instantiate three 5-bit counters
countUD5L counter0 (
    .clk(clk),
    .UD(UD),
    .CE(CE),
    .LD(LD),
    .Din(Din[4:0]),
    .Q(Q0),
    .UTC(UTC0),
    .DTC(DTC0)
);

countUD5L counter1 (
    .clk(clk),
    .UD(UD),
    // For incrementing, enable next counter on UTC. For decrementing, check DTC & !UD.
    .CE((UD & CE & UTC0) | (~UD & CE & DTC0)),
    .LD(LD),
    .Din(Din[9:5]),
    .Q(Q1),
    .UTC(UTC1),
    .DTC(DTC1)
);

countUD5L counter2 (
    .clk(clk),
    .UD(UD),
    .CE((UD & CE & UTC1 & UTC0) | (~UD & CE & DTC1 & DTC0)),
    .LD(LD),
    .Din(Din[14:10]),
    .Q(Q2),
    .UTC(UTC2),
    .DTC(DTC2)
);

// Combine the outputs of the three counters
assign Q = {Q2, Q1, Q0};

// UTC and DTC logic for the entire 15-bit counter
assign UTC = UTC2 & UTC1 & UTC0; // 15-bit counter is at max when the most significant 5-bit counter is at UTC
assign DTC = DTC0 & DTC1 & DTC2; // 15-bit counter is at min only when all counters are at DTC

endmodule
