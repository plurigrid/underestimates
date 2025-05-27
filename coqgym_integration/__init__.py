"""
CoqGym Integration for Automated Theorem Proving in Analysis

This module implements a neural network-based approach to automatically prove
or verify estimates in analysis, demonstrating aspects of the halting problem
through the undecidability of certain proof verification tasks.
"""

from .halting_problem import HaltingProblemDemonstrator
from .proof_environment import ProofEnvironment
from .neural_prover import NeuralProver
from .estimate_verifier import EstimateVerifier

__all__ = [
    'HaltingProblemDemonstrator',
    'ProofEnvironment', 
    'NeuralProver',
    'EstimateVerifier'
]