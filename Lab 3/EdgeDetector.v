`timescale 1ns / 1ps

module EdgeDetector(
    input clk,
    input signal,
    output edge_detected
);

// Wires to connect FDRE outputs
wire current_state, previous_state;

// FDRE for current state
FDRE #(.INIT(1'b0)) fdre_current (
    .C(clk),
    .CE(1'b1),  // enabled
    .R(1'b0),   // No reset I DISABLED RESET
    .D(signal),
    .Q(current_state)
);

// FDRE for previous state
FDRE #(.INIT(1'b0)) fdre_previous (
    .C(clk),
    .CE(1'b1),  // enabled
    .R(1'b0),   // No reset I DISABLED RESET
    .D(current_state),
    .Q(previous_state)
);

// Detect rising edge
assign edge_detected = ~previous_state & current_state;

endmodule
