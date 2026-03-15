# SCENARIO 2 QUICK REFERENCE

## 🎯 What Is This?

Inner city navigation experiment testing driver suggestibility when audio cues conflict with correct route.

**Key Test:** At buildings intersection, audio says "go straight" but driver should turn RIGHT.

---

## 🚀 Quick Run (3 Commands)

```powershell
# Terminal 1
CarlaUE4.exe

# Terminal 2
conda activate carla13
python manual_control.py

# Terminal 3
conda activate carla13
python run_scenario2.py
```

---

## 📍 Route Map

```
START (elevated)
    ↓
First Entrance [TRUE: straight]
    ↓
City Center [TRUE: straight]
    ↓
Buildings ⚠️ [FALSE: says straight, should turn RIGHT]
    ↓
Barriers [TRUE: straight]
    ↓
END (elevated)
```

---

## ⚙️ Key Settings

```python
# Visual
Dot spacing: 8 meters
Fade start: 80 meters before intersection
Fade end: At intersection (0m)

# Audio
Warning: 80m before ("In 80 meters...")
Command: 12m before ("Turn now")

# Deception
Intersection 3: Audio says STRAIGHT
Correct action: RIGHT
```

---

## 📊 What Gets Logged

Every run creates in `experiment_logs/`:

1. **telemetry_[time].csv** - Position, speed (20 Hz)
2. **events_[time].csv** - Audio cues, reroutes
3. **decisions_[time].csv** - Driver choices
4. **summary_[time].json** - Overall stats

**Key Metric:** Did driver turn RIGHT or go STRAIGHT at Intersection 3?

---

## 🎮 Driver Controls

```
W - Gas
S - Brake
A - Steer left
D - Steer right

9 - Bird's eye view
TAB - Cycle cameras
```

---

## ⚠️ Troubleshooting

**No blue dots?**
→ Check console: "Path calculated with X waypoints"

**No audio?**
→ `pip install pygame`
→ Check audio files in scenarios/audio/

**Two vehicles?**
→ Run manual_control.py BEFORE run_scenario2.py

**Can't find vehicle?**
→ Make sure manual_control.py spawned a Tesla

---

## 📁 Files You Need

```
run_scenario2.py          ← Main runner
scenario2_route.py        ← Route definition
scenario2_config.py       ← Settings

From core/:
- main_experiment.py
- experiment_config.py
- pathfinding.py
- visual_guidance.py
- audio_manager.py
- data_logger.py

From scenarios/audio/:
- All 6 .wav files
```

---

## 🎓 Quick Analysis

```python
import pandas as pd

# Load decisions
df = pd.read_csv('experiment_logs/decisions_TIMESTAMP.csv')

# Check Intersection 3 (index 2)
i3 = df[df['intersection_id'] == 2]

# Result
if i3['driver_action'].values[0] == 'straight':
    print("Followed FALSE audio (suggestible)")
elif i3['driver_action'].values[0] == 'right':
    print("Ignored FALSE audio (correct)")
```

---

## ✅ Pre-Flight Checklist

Before running:
- [ ] CARLA running
- [ ] pygame installed
- [ ] Audio files exist
- [ ] manual_control.py spawned vehicle
- [ ] In correct directory

---

## 📞 Quick Help

**Path calculation fails:**
- Coordinates might be off-road
- Check console for "No path found"

**Audio doesn't play:**
- Volume up?
- Files in scenarios/audio/?
- pygame installed?

**Visuals choppy:**
- CARLA graphics settings
- Close other programs

---

**Ready to run?** Just execute the 3 terminal commands above! 🚗
