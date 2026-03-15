"""
Scenario 1 Experiment Runner
Ready-to-run script for basic suggestibility test
"""

import sys
import time

# Import scenario-specific configurations
from scenario1_config import Scenario1Config
from scenario1_route import Scenario1Route

# Import the main experiment controller
from main_experiment import SuggestibilityExperiment


def print_scenario_info():
    """Print scenario information before starting"""
    print("\n" + "="*70)
    print("SCENARIO 1: BASIC SUGGESTIBILITY TEST")
    print("="*70)
    print("\nRoute Overview:")
    print("  Start: West of town (-147.0, 1.3, 0.5)")
    print("  Path:  Straight road with 3 checkpoints")
    print("  End:   Town center (0.0, 1.3, 0.5)")
    print("\nIntersections:")
    print("  1. First checkpoint (TRUE cue)")
    print("  2. Mid-route checkpoint (TRUE cue)")
    print("  3. Final checkpoint (FALSE cue - STRAIGHT vs RIGHT) ⚠️")
    print("\nObjective:")
    print("  Establish baseline suggestibility measurement with simple route.")
    print("  After two correct cues, test if driver follows false RIGHT cue")
    print("  when the correct action is to continue STRAIGHT.")
    print("\n" + "="*70 + "\n")


def main():
    """
    Main entry point for Scenario 1 experiment
    """
    # Print scenario information
    print_scenario_info()
    
    # Verify prerequisites
    print("Checking prerequisites...")
    print("  ✓ Make sure CARLA is running (CarlaUE4.exe)")
    print("  ✓ Make sure manual_control.py is running (spawned vehicle)")
    print("  ✓ Audio files are in correct directory")
    
    input("\nPress ENTER when ready to start experiment...")
    
    # Create scenario-specific configuration
    config = Scenario1Config()
    route = Scenario1Route()
    
    # Print route description
    print("\n" + route.get_route_description())
    
    # Create and run experiment
    try:
        print("\nInitializing Scenario 1 experiment...")
        experiment = SuggestibilityExperiment(config, route)
        
        print("Starting experiment...\n")
        experiment.run_experiment()
        
    except KeyboardInterrupt:
        print("\n\nExperiment stopped by user")
    except Exception as e:
        print(f"\n\nError running experiment: {e}")
        import traceback
        traceback.print_exc()
    
    print("\nScenario 1 experiment complete.")


if __name__ == "__main__":
    main()
