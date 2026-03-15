# Scenario 2: Inner City Navigation

## Overview

This scenario tests driver suggestibility in an urban environment where visual cues fade before a critical decision point.

## Route Description

**Start Position:** Elevated area outside the city  
**End Position:** Outside city on opposite side  
**Total Distance:** ~450 meters  
**Number of Intersections:** 4  
**Deceptive Trials:** 1 (Intersection 3)

### Route Waypoints

1. **Start** (-232.45, 129.72, 10.00) - Elevated position
2. **First Entrance** (33.21, 181.05, 0.00) - Entry to inner city
3. **City Center** (30.98, 2.52, 0.00) - Central navigation point
4. **Buildings Intersection** (-123.72, 2.33, 0.00) - **Critical deceptive point**
5. **Barriers Area** (-123.35, 132.38, 0.00) - Near barriers
6. **End** (-237.81, 64.35, 10.00) - Exit city

## Intersections

### Intersection 1: First Entrance (TRUE CUE)
- **Location:** (33.21, 181.05, 0.00)
- **Correct Action:** STRAIGHT
- **Audio:** "Continue straight" ✓
- **Purpose:** Establish trust in navigation system

### Intersection 2: City Center (TRUE CUE)
- **Location:** (30.98, 2.52, 0.00)
- **Correct Action:** STRAIGHT
- **Audio:** "Continue straight" ✓
- **Purpose:** Reinforce trust before deceptive trial

### Intersection 3: Buildings (FALSE CUE) ⚠️
- **Location:** (-123.72, 2.33, 0.00)
- **Correct Action:** RIGHT
- **Audio Says:** "Continue straight" ✗
- **Purpose:** **PRIMARY SUGGESTIBILITY TEST**
- **Note:** Visual waypoints have faded by this point (100m fade)

### Intersection 4: Barriers Area (TRUE CUE)
- **Location:** (-123.35, 132.38, 0.00)
- **Correct Action:** STRAIGHT
- **Audio:** "Continue straight" ✓
- **Purpose:** Post-deception navigation

## Experimental Design

### Hypothesis
Drivers who have built trust through correct initial cues will be more likely to follow the false audio cue at Intersection 3, even when it conflicts with the correct route.

### Visual Manipulation
- Blue waypoint dots are visible up to 100m before each intersection
- Dots fade progressively from 100m to 0m
- At the critical deceptive intersection (Intersection 3), visual cues have completely disappeared
- Driver must rely on either:
  - Memory of the route
  - Audio instructions (which are incorrect)
  - Intuition/environmental cues

### Measured Variables
1. **Primary:** Did driver follow false audio cue? (turn vs. straight)
2. **Secondary:** Reaction time from audio cue to decision
3. **Secondary:** Correction time if driver initially followed false cue
4. **Secondary:** Path deviation metrics

## Configuration

Optimized for urban environment:

```python
# Visual Settings
WAYPOINT_SPACING = 8.0        # Tighter spacing for city
WAYPOINT_HEIGHT = 1.2         # Higher for visibility between buildings
WAYPOINT_FADE_START = 80.0    # Earlier fade in tight streets
WAYPOINT_SIZE = 0.35          # Larger dots for city visibility

# Audio Settings
AUDIO_WARNING_DISTANCE = 80.0  # Closer warning in city
AUDIO_COMMAND_DISTANCE = 12.0  # Slightly earlier command

# Pathfinding
REROUTE_THRESHOLD = 12.0      # Tighter threshold for city streets
```

## Running Scenario 2

### Quick Run

```bash
# Terminal 1: CARLA
CarlaUE4.exe

# Terminal 2: Manual Control
conda activate carla13
python manual_control.py

# Terminal 3: Scenario 2
conda activate carla13
python scenarios/scenario2/run_scenario2.py
```

### What to Expect

**Console Output:**
```
SCENARIO 2: INNER CITY NAVIGATION
==================================
Route Overview:
  Start: Elevated position outside city
  Path:  First entrance → City center → Buildings → Barriers → Exit
  End:   Outside city

Intersections:
  1. First entrance (TRUE cue)
  2. City center (TRUE cue)
  3. Buildings intersection (FALSE cue - RIGHT vs STRAIGHT) ⚠️
  4. Barriers area (TRUE cue)

✓ Path calculated with 56 waypoints
✓ Audio loading complete. 6 files loaded.
```

**In CARLA:**
- Blue dots every 8 meters
- Dots fade starting 80m before each intersection
- At Intersection 3, no visual cues present
- Audio says "Continue straight" (incorrect)
- Correct action is to turn RIGHT

## Data Analysis

### Key Metrics for Scenario 2

```python
import pandas as pd

# Load data
decisions = pd.read_csv('experiment_logs/decisions_*.csv')

# Focus on Intersection 3 (the deceptive trial)
intersection_3 = decisions[decisions['intersection_id'] == 2]  # 0-indexed

# Did driver follow false cue?
followed_false = (intersection_3['driver_action'] == 'straight').values[0]
correct_decision = (intersection_3['driver_action'] == 'right').values[0]

print(f"Followed false audio: {followed_false}")
print(f"Made correct decision: {correct_decision}")
print(f"Reaction time: {intersection_3['reaction_time'].values[0]:.2f}s")
```

### Expected Results

Based on suggestibility research:
- **High Trust Drivers:** 60-70% follow false cue (go straight)
- **Medium Trust Drivers:** 30-50% follow false cue
- **Low Trust Drivers:** 10-20% follow false cue

Factors affecting suggestibility:
- Prior experience with navigation systems
- Confidence in spatial memory
- Attention to visual cues before they faded
- General trust in automation

## Customization

### Adjusting Deception Location

Edit `scenario2_route.py`:

```python
# Change which intersection is deceptive
intersections[2]['is_deceptive'] = True  # Make intersection 3 deceptive
intersections[3]['is_deceptive'] = False  # Remove deception from intersection 4
```

### Changing Fade Timing

Edit `scenario2_config.py`:

```python
# Make visual cues disappear earlier
WAYPOINT_FADE_START = 120.0  # Start fading at 120m (was 80m)

# Or make them stay longer
WAYPOINT_FADE_START = 50.0   # Start fading at 50m
```

### Adding More Deceptive Trials

```python
# In scenario2_route.py
intersections.append({
    'location': carla.Location(x=X, y=Y, z=Z),
    'correct_action': 'left',
    'is_deceptive': True,
    'deceptive_action': 'right',
    'trial_number': 5
})
```

## Tips for Running

1. **Practice Run:** Do a practice run with all TRUE cues first to familiarize drivers with the route
2. **Counterbalancing:** Alternate which intersection is deceptive across participants
3. **Debriefing:** Ask drivers post-experiment if they noticed the false cue
4. **Trust Calibration:** Consider adding a trust questionnaire before/after

## Troubleshooting

**Driver keeps going off-route:**
- Path calculation might be failing - check console for errors
- Adjust `REROUTE_THRESHOLD` in config to be more forgiving

**Can't see blue dots in city:**
- Increase `WAYPOINT_SIZE` to 0.4 or 0.5
- Increase `WAYPOINT_HEIGHT` to 1.5 or 2.0

**Audio cues too late/early:**
- Adjust `AUDIO_WARNING_DISTANCE` and `AUDIO_COMMAND_DISTANCE`
- City streets may need closer warnings (60-70m)

---

**Ready to test suggestibility?** Run the scenario and analyze the results! 🚗🧠
