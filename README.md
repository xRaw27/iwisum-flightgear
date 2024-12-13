# IWISUM project - Reinformcement Learning with FlightGear

## Dariusz Piwowarski, Wojciech Przybytek

### Resources

- [FlightGear](https://www.flightgear.org)
- [JSBSim](https://github.com/JSBSim-Team/jsbsim)
- [jsbgym](https://github.com/sryu1/jsbgym)

### Introduction

The goal of this project is to create an autopiolt for a Cessna 172P aircraft in FlightGear using reinforcement
learning.

### FlightGear setup on MacOS

Add the following to your `~/.zshrc` or `~/.bashrc` file:

```bash
export PATH="/Applications/FlightGear.app/Contents/MacOS:$PATH"
export FG_ROOT="/Applications/FlightGear.app/Contents/Resources"
```

For Windows/Linux follow the instructions from [jsbgym setup](https://github.com/sryu1/jsbgym?tab=readme-ov-file#setup)
