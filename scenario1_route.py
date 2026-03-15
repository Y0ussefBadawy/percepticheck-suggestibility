"""
Scenario 1 Route Configuration
Basic suggestibility test with simple route
"""

import carla


class Scenario1Route:
    """
    Route configuration for Scenario 1
    
    Route Overview:
    - Simple straight route with turns
    - 3 intersections total
    - 1 deceptive trial at the end
    
    Purpose: Baseline suggestibility measurement
    """
    
    def __init__(self):
        # Define the complete route waypoints
        self.waypoints = [
            # Starting point
            carla.Location(x=-147.0, y=1.3, z=0.5),
            
            # First turn point
            carla.Location(x=-100.0, y=1.3, z=0.5),
            
            # Second turn point
            carla.Location(x=-50.0, y=1.3, z=0.5),
            
            # Final destination
            carla.Location(x=0.0, y=1.3, z=0.5),
        ]
        
        # Define intersections with audio cues
        self.intersections = [
            # Intersection 1: First turn (TRUE cue)
            {
                'location': carla.Location(x=-120.0, y=1.3, z=0.5),
                'correct_action': 'straight',
                'trial_number': 1,
                'is_deceptive': False,  # TRUE audio - guides correctly
                'description': 'First checkpoint (establish trust)'
            },
            
            # Intersection 2: Mid-route (TRUE cue)
            {
                'location': carla.Location(x=-75.0, y=1.3, z=0.5),
                'correct_action': 'straight',
                'trial_number': 2,
                'is_deceptive': False,  # TRUE audio
                'description': 'Mid-route checkpoint (reinforce trust)'
            },
            
            # Intersection 3: Final decision (DECEPTIVE cue)
            {
                'location': carla.Location(x=-25.0, y=1.3, z=0.5),
                'correct_action': 'straight',
                'trial_number': 3,
                'is_deceptive': True,  # FALSE audio - test suggestibility!
                'deceptive_action': 'right',  # Audio says right, but should go straight
                'description': 'Final checkpoint (DECEPTIVE TRIAL)'
            },
        ]
        
        # Deceptive actions mapping
        self.deceptive_actions = {
            2: 'right',  # Intersection 3: audio says 'right' but correct is 'straight'
        }
    
    def get_destination(self):
        """Returns the final destination waypoint"""
        return self.waypoints[-1]
    
    def get_deceptive_action(self, intersection_index):
        """Returns the false action for a deceptive trial"""
        return self.deceptive_actions.get(intersection_index, None)
    
    def get_start_location(self):
        """Returns the starting location"""
        return self.waypoints[0]
    
    def get_route_description(self):
        """Returns a description of the route"""
        return (
            "Scenario 1: Basic Suggestibility Test\n"
            "======================================\n"
            "Start: Road position west of town\n"
            "Route: Straight path with 3 checkpoints\n"
            "Total Intersections: 3 (2 true cues, 1 false cue)\n"
            "Deceptive Trial: Intersection 3 (final checkpoint)\n"
            "  - Correct action: STRAIGHT\n"
            "  - Audio says: RIGHT (false cue)\n"
        )


# For easy import
def get_scenario1_route():
    """Helper function to get Scenario 1 route"""
    return Scenario1Route()


if __name__ == "__main__":
    # Test the route configuration
    route = Scenario1Route()
    print(route.get_route_description())
    print(f"\nTotal waypoints: {len(route.waypoints)}")
    print(f"Total intersections: {len(route.intersections)}")
    print(f"\nIntersections:")
    for i, intersection in enumerate(route.intersections):
        deceptive = " [DECEPTIVE]" if intersection.get('is_deceptive') else ""
        print(f"  {i+1}. {intersection['description']}{deceptive}")
        print(f"     Location: x={intersection['location'].x:.2f}, y={intersection['location'].y:.2f}")
        print(f"     Action: {intersection['correct_action']}")
