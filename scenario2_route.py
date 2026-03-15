"""
Scenario 2 Route Configuration
Inner city route with two entrance options
"""

import carla


class Scenario2Route:
    """
    Route configuration for Scenario 2
    
    Route Overview:
    - Start: Outside the city (elevated position)
    - Two possible entrances to inner city
    - Main path through city center
    - End: Outside city on opposite side
    
    Key Decision Points:
    1. First entrance vs Second entrance (entrance selection)
    2. Straight through city center
    3. Right turn at intersection between buildings
    4. Navigate to barriers area
    """
    
    def __init__(self):
        # Define the complete route waypoints
        self.waypoints = [
            # Starting point (elevated, outside city)
            carla.Location(x=-232.45, y=129.72, z=10.00),
            
            # First entrance to inner city
            carla.Location(x=33.21, y=181.05, z=0.00),
            
            # City center navigation point
            carla.Location(x=30.98, y=2.52, z=0.00),
            
            # Intersection between buildings
            carla.Location(x=-123.72, y=2.33, z=0.00),
            
            # Barriers area
            carla.Location(x=-123.35, y=132.38, z=0.00),
            
            # Final destination (outside city)
            carla.Location(x=-237.81, y=64.35, z=10.00),
        ]
        
        # Alternative entrance option (second entrance)
        self.second_entrance = carla.Location(x=30.12, y=-181.11, z=0.00)
        
        # Define intersections with audio cues
        self.intersections = [
            # Intersection 1: Entrance selection
            {
                'location': carla.Location(x=33.21, y=181.05, z=0.00),
                'correct_action': 'straight',  # Continue to first entrance
                'trial_number': 1,
                'is_deceptive': False,  # TRUE audio - guides correctly
                'description': 'First entrance to inner city'
            },
            
            # Intersection 2: City center - proceed straight
            {
                'location': carla.Location(x=30.98, y=2.52, z=0.00),
                'correct_action': 'straight',
                'trial_number': 2,
                'is_deceptive': False,  # TRUE audio
                'description': 'City center navigation'
            },
            
            # Intersection 3: Turn right at buildings
            {
                'location': carla.Location(x=-123.72, y=2.33, z=0.00),
                'correct_action': 'right',
                'trial_number': 3,
                'is_deceptive': True,  # FALSE audio - test suggestibility!
                'deceptive_action': 'straight',  # Audio says straight, but should turn right
                'description': 'Intersection between buildings (DECEPTIVE TRIAL)'
            },
            
            # Intersection 4: Approach barriers
            {
                'location': carla.Location(x=-123.35, y=132.38, z=0.00),
                'correct_action': 'straight',
                'trial_number': 4,
                'is_deceptive': False,  # TRUE audio
                'description': 'Barriers area'
            },
        ]
        
        # Deceptive actions mapping
        self.deceptive_actions = {
            2: 'straight',  # Intersection 3: audio says 'straight' but correct is 'right'
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
            "Scenario 2: Inner City Navigation\n"
            "=================================\n"
            "Start: Elevated position outside city\n"
            "Route: First entrance → City center → Right turn at buildings → Barriers → Exit\n"
            "Total Intersections: 4 (3 true cues, 1 false cue)\n"
            "Deceptive Trial: Intersection 3 (buildings intersection)\n"
            "  - Correct action: RIGHT\n"
            "  - Audio says: STRAIGHT (false cue)\n"
        )


# For easy import
def get_scenario2_route():
    """Helper function to get Scenario 2 route"""
    return Scenario2Route()


if __name__ == "__main__":
    # Test the route configuration
    route = Scenario2Route()
    print(route.get_route_description())
    print(f"\nTotal waypoints: {len(route.waypoints)}")
    print(f"Total intersections: {len(route.intersections)}")
    print(f"\nIntersections:")
    for i, intersection in enumerate(route.intersections):
        deceptive = " [DECEPTIVE]" if intersection.get('is_deceptive') else ""
        print(f"  {i+1}. {intersection['description']}{deceptive}")
        print(f"     Location: x={intersection['location'].x:.2f}, y={intersection['location'].y:.2f}")
        print(f"     Action: {intersection['correct_action']}")
