OBSERVATION_SPACE = [
    ('position/h-sl-ft', 'altitude above mean sea level [ft]', -1400, 85000),
    ('attitude/pitch-rad', 'pitch [rad]', -1.5707963267948966, 1.5707963267948966),
    ('attitude/roll-rad', 'roll [rad]', -3.141592653589793, 3.141592653589793),
    ('velocities/u-fps', 'body frame x-axis velocity [ft/s]', -2200, 2200),
    ('velocities/v-fps', 'body frame y-axis velocity [ft/s]', -2200, 2200),
    ('velocities/w-fps', 'body frame z-axis velocity [ft/s]', -2200, 2200),
    ('velocities/p-rad_sec', 'roll rate [rad/s]', -6.283185307179586, 6.283185307179586),
    ('velocities/q-rad_sec', 'pitch rate [rad/s]', -6.283185307179586, 6.283185307179586),
    ('velocities/r-rad_sec', 'yaw rate [rad/s]', -6.283185307179586, 6.283185307179586),
    ('error/altitude-error-ft', 'error to desired altitude [ft]', -1400, 85000),
    ('error/track-error-deg', 'error to desired track [deg]', -180, 180),
]

ACTION_SPACE = [
    ('fcs/aileron-cmd-norm', 'aileron commanded position, normalised', -1.0, 1.0),
    ('fcs/elevator-cmd-norm', 'elevator commanded position, normalised', -1.0, 1.0),
    ('fcs/rudder-cmd-norm', 'rudder commanded position, normalised', -1.0, 1.0),
]
