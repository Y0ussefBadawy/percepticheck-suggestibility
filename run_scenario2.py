"""
Scenario 2 Experiment Runner
Ready-to-run script for inner city navigation experiment
"""

import sys
import time

# Import scenario-specific configurations
from scenario2_config import Scenario2Config
from scenario2_route import Scenario2Route

# Import the main experiment controller
from main_experiment import SuggestibilityExperiment


def print_scenario_info():
    """Print scenario information before starting"""
    print("\n" + "="*70)
    print("SCENARIO 2: INNER CITY NAVIGATION")
    print("="*70)
    print("\nRoute Overview:")
    print("  Start: Elevated position outside city (-232.45, 129.72, 10.00)")
    print("  Path:  First entrance → City center → Buildings → Barriers → Exit")
    print("  End:   Outside city (-237.81, 64.35, 10.00)")
    print("\nIntersections:")
    print("  1. First entrance (TRUE cue)")
    print("  2. City center (TRUE cue)")
    print("  3. Buildings intersection (FALSE cue - RIGHT vs STRAIGHT) ⚠️")
    print("  4. Barriers area (TRUE cue)")
    print("\nObjective:")
    print("  Test driver suggestibility at the buildings intersection where")
    print("  audio incorrectly instructs to go straight instead of turning right.")
    print("\n" + "="*70 + "\n")


def main():
    """
    Main entry point for Scenario 2 experiment
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
    config = Scenario2Config()
    route = Scenario2Route()
    
    # Print route description
    print("\n" + route.get_route_description())
    
    # Create and run experiment
    try:
        print("\nInitializing Scenario 2 experiment...")
        experiment = SuggestibilityExperiment(config, route)
        
        print("Starting experiment...\n")
        experiment.run_experiment()
        
    except KeyboardInterrupt:
        print("\n\nExperiment stopped by user")
    except Exception as e:
        print(f"\n\nError running experiment: {e}")
        import traceback
        traceback.print_exc()
    
    print("\nScenario 2 experiment complete.")


if __name__ == "__main__":
    main()
