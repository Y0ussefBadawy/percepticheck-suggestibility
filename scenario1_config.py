"""
Scenario 1 Experiment Configuration
Simple baseline suggestibility test
"""

import carla
from experiment_config import ExperimentConfig


class Scenario1Config(ExperimentConfig):
    """
    Configuration specific to Scenario 1
    Simple baseline test - inherits from base ExperimentConfig
    """
    
    def __init__(self):
        # Call parent constructor
        super().__init__()
        
        # Override spawn location for Scenario 1
        self.SPAWN_LOCATION = carla.Location(x=-147.0, y=1.3, z=0.5)
        self.SPAWN_ROTATION = carla.Rotation(pitch=0.0, yaw=0.0, roll=0.0)
        
        # Visual settings - standard defaults work well for open road
        self.WAYPOINT_SPACING = 10.0  # Standard spacing
        self.WAYPOINT_HEIGHT = 1.0    # Standard height
        self.WAYPOINT_FADE_START = 100.0  # Standard fade
        self.WAYPOINT_FADE_END = 0.0      # Complete fade
        self.WAYPOINT_SIZE = 0.3          # Standard size
        
        # Audio settings - standard timings
        self.AUDIO_WARNING_DISTANCE = 100.0  # Standard warning
        self.AUDIO_COMMAND_DISTANCE = 10.0   # Standard command
        
        # Pathfinding - standard threshold
        self.REROUTE_THRESHOLD = 15.0  # Standard reroute threshold
        
        # Experiment-specific settings
        self.SCENARIO_NAME = "Scenario 1: Basic Suggestibility Test"
        self.SCENARIO_DESCRIPTION = (
            "Simple straight route with 3 checkpoints, "
            "testing basic suggestibility with final deceptive cue"
        )


def get_scenario1_config():
    """Helper function to get Scenario 1 configuration"""
    return Scenario1Config()
