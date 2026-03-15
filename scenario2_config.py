"""
Scenario 2 Experiment Configuration
Overrides default settings for inner city navigation scenario
"""

import carla
from experiment_config import ExperimentConfig


class Scenario2Config(ExperimentConfig):
    """
    Configuration specific to Scenario 2
    Inherits from base ExperimentConfig and overrides relevant settings
    """
    
    def __init__(self):
        # Call parent constructor
        super().__init__()
        
        # Override spawn location for Scenario 2 (elevated start position)
        self.SPAWN_LOCATION = carla.Location(x=-232.45, y=129.72, z=10.00)
        self.SPAWN_ROTATION = carla.Rotation(pitch=0.0, yaw=90.0, roll=0.0)  # Facing toward city
        
        # Visual settings optimized for inner city
        self.WAYPOINT_SPACING = 8.0  # Slightly tighter spacing for city navigation (was 10.0)
        self.WAYPOINT_HEIGHT = 1.2   # Higher for better visibility in dense city (was 1.0)
        self.WAYPOINT_FADE_START = 80.0  # Start fading earlier in tight city streets (was 100.0)
        self.WAYPOINT_FADE_END = 0.0     # Complete fade at intersection
        self.WAYPOINT_SIZE = 0.35        # Slightly larger for city visibility (was 0.3)
        
        # Audio settings - adjusted for city environment
        self.AUDIO_WARNING_DISTANCE = 80.0   # Closer warning in city (was 100.0)
        self.AUDIO_COMMAND_DISTANCE = 12.0   # Slightly earlier command (was 10.0)
        
        # Pathfinding - tighter threshold for city streets
        self.REROUTE_THRESHOLD = 12.0  # Reroute sooner in dense city (was 15.0)
        
        # Experiment-specific settings
        self.SCENARIO_NAME = "Scenario 2: Inner City Navigation"
        self.SCENARIO_DESCRIPTION = (
            "Navigate from elevated start position through inner city, "
            "testing suggestibility at the buildings intersection"
        )


def get_scenario2_config():
    """Helper function to get Scenario 2 configuration"""
    return Scenario2Config()
