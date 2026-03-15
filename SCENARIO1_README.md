# Scenario 1: Basic Suggestibility Test

## Overview

This is the baseline scenario for measuring driver suggestibility in a simple, controlled environment.

## Route Description

**Start Position:** Road west of town  
**End Position:** Town center  
**Total Distance:** ~150 meters  
**Number of Intersections:** 3  
**Deceptive Trials:** 1 (Intersection 3)

### Route Waypoints

1. **Start** (-147.0, 1.3, 0.5) - West of town
2. **Waypoint 1** (-100.0, 1.3, 0.5) - First checkpoint area
3. **Waypoint 2** (-50.0, 1.3, 0.5) - Mid-route
4. **End** (0.0, 1.3, 0.5) - Town center

## Intersections

### Intersection 1: First Checkpoint (TRUE CUE)
- **Location:** (-120.0, 1.3, 0.5)
- **Correct Action:** STRAIGHT
- **Audio:** "Continue straight" ✓
- **Purpose:** Establish initial trust in the navigation system

### Intersection 2: Mid-Route Checkpoint (TRUE CUE)
- **Location:** (-75.0, 1.3, 0.5)
- **Correct Action:** STRAIGHT
- **Audio:** "Continue straight" ✓
- **Purpose:** Reinforce trust through consistent correct guidance

### Intersection 3: Final Checkpoint (FALSE CUE) ⚠️
- **Location:** (-25.0, 1.3, 0.5)
- **Correct Action:** STRAIGHT
- **Audio Says:** "Turn right" ✗
- **Purpose:** **PRIMARY SUGGESTIBILITY TEST**
- **Note:** Visual waypoints have faded (100m fade range)

## Experimental Design

### Hypothesis
After establishing trust through two correct audio cues, drivers will be more likely to follow the false "turn right" instruction at the final checkpoint, even though continuing straight is correct.

### Control Features
- **Simple Route:** Straight path minimizes navigation complexity
- **Consistent Environment:** Open road without confounding variables
- **Clear Decision Point:** Final intersection is unambiguous
- **Trust Building:** Two correct cues before deceptive cue

### Visual Manipulation
- Blue waypoint dots visible up to 100m before each intersection
- Dots fade progressively from 100m to 0m
- At final checkpoint (deceptive trial), visual cues are completely gone
- Driver must choose between:
  - Memory of straight path
  - Audio instruction to turn right
  - Visual environment cues

### Measured Variables
1. **Primary:** Did driver turn right (follow false audio) or continue straight (correct)?
2. **Secondary:** Reaction time from audio cue to decision
3. **Secondary:** Hesitation indicators (speed reduction, steering corrections)
4. **Secondary:** Path deviation if driver initially followed false cue

## Configuration

Standard settings for open road:

```python
# Visual Settings
WAYPOINT_SPACING = 10.0       # Standard spacing
WAYPOINT_HEIGHT = 1.0         # Standard height
WAYPOINT_FADE_START = 100.0   # Standard fade distance
WAYPOINT_SIZE = 0.3           # Standard size

# Audio Settings
AUDIO_WARNING_DISTANCE = 100.0  # "In 100m, turn right"
AUDIO_COMMAND_DISTANCE = 10.0   # "Turn right now"

# Pathfinding
REROUTE_THRESHOLD = 15.0      # Standard threshold
```

## Running Scenario 1

### Quick Run

```bash
# Terminal 1: CARLA
CarlaUE4.exe

# Terminal 2: Manual Control
conda activate carla13
python manual_control.py

# Terminal 3: Scenario 1
conda activate carla13
python scenarios/scenario1/run_scenario1.py
```

### What to Expect

**Console Output:**
```
SCENARIO 1: BASIC SUGGESTIBILITY TEST
======================================
Route Overview:
  Start: West of town
  Path:  Straight road with 3 checkpoints
  End:   Town center

Intersections:
  1. First checkpoint (TRUE cue)
  2. Mid-route checkpoint (TRUE cue)
  3. Final checkpoint (FALSE cue - STRAIGHT vs RIGHT) ⚠️

✓ Path calculated with 30 waypoints
✓ Audio loading complete. 6 files loaded.
```

**In CARLA:**
- Straight road heading east
- Blue dots every 10 meters
- Dots fade as you approach each checkpoint
- At final checkpoint, audio says "Turn right" but path continues straight
- No visual cues at final decision point

## Data Analysis

### Key Metrics for Scenario 1

```python
import pandas as pd

# Load data
decisions = pd.read_csv('experiment_logs/decisions_*.csv')

# Focus on Intersection 3 (the deceptive trial)
intersection_3 = decisions[decisions['intersection_id'] == 2]  # 0-indexed

# Did driver follow false cue?
followed_false = (intersection_3['driver_action'] == 'right').values[0]
correct_decision = (intersection_3['driver_action'] == 'straight').values[0]

print(f"Followed false audio (turned right): {followed_false}")
print(f"Made correct decision (went straight): {correct_decision}")
print(f"Reaction time: {intersection_3['reaction_time'].values[0]:.2f}s")
```

### Expected Results

Based on trust and automation bias research:

**High Suggestibility Condition (60-80% follow false cue):**
- New drivers
- High trust in technology
- Low confidence in spatial memory
- Distracted or cognitively loaded

**Medium Suggestibility Condition (30-50% follow false cue):**
- Experienced drivers
- Moderate trust in navigation systems
- Balanced reliance on multiple cues

**Low Suggestibility Condition (10-20% follow false cue):**
- Professional drivers
- Low automation trust
- High confidence in own navigation
- Explicitly warned about potential errors

### Comparative Analysis

Compare Scenario 1 (simple route) with Scenario 2 (complex city):

```python
# Load both scenarios
s1_decisions = pd.read_csv('experiment_logs/scenario1_decisions.csv')
s2_decisions = pd.read_csv('experiment_logs/scenario2_decisions.csv')

# Compare suggestibility rates
s1_deceptive = s1_decisions[s1_decisions['is_deceptive'] == True]
s2_deceptive = s2_decisions[s2_decisions['is_deceptive'] == True]

s1_followed = (s1_deceptive['driver_action'] == s1_deceptive['audio_action']).mean()
s2_followed = (s2_deceptive['driver_action'] == s2_deceptive['audio_action']).mean()

print(f"Scenario 1 suggestibility: {s1_followed*100:.1f}%")
print(f"Scenario 2 suggestibility: {s2_followed*100:.1f}%")
```

**Hypothesis:** Scenario 2 (city) should show higher suggestibility due to increased cognitive load.

## Customization

### Adjusting Deception Type

Edit `scenario1_route.py`:

```python
# Change what false audio says
intersections[2]['deceptive_action'] = 'left'  # Instead of 'right'
```

### Adding More Deceptive Trials

```python
# Make intersection 2 also deceptive
intersections[1]['is_deceptive'] = True
intersections[1]['deceptive_action'] = 'right'
```

### Changing Route Length

```python
# Extend the route
waypoints.append(carla.Location(x=50.0, y=1.3, z=0.5))
waypoints.append(carla.Location(x=100.0, y=1.3, z=0.5))
```

## Research Applications

### Baseline Measurement
Use Scenario 1 to establish individual driver's baseline suggestibility before more complex scenarios.

### Training Effect Study
Run Scenario 1 multiple times to see if drivers learn to distrust false cues.

### Individual Differences
Correlate Scenario 1 performance with personality measures:
- Trust in automation
- Need for cognitive closure
- Locus of control
- Driving experience

### Intervention Testing
Test different interventions:
- Warning about potential false cues
- Training on visual cue interpretation
- Confidence calibration exercises

## Tips for Running

1. **Pilot Testing:** Run 2-3 practice participants to verify route and timing
2. **Consistent Instructions:** Give all participants same pre-experiment briefing
3. **Attention Check:** Consider adding attention check questions post-experiment
4. **Debriefing:** Ask "Did you notice anything unusual about the navigation?"

## Troubleshooting

**Driver doesn't reach final intersection:**
- Check that route waypoints are on valid roads
- Verify spawn location is accessible

**Audio cues misaligned:**
- Adjust `AUDIO_WARNING_DISTANCE` if cues come too early/late
- Check intersection locations are accurate

**No suggestibility effect:**
- Verify audio is audible and clear
- Check that visual cues are properly fading
- Confirm deceptive trial is actually false

---

**Scenario 1 is your baseline.** Start here before running more complex scenarios! 🚗📊
