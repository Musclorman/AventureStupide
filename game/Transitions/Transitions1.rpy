transform LtoR:
    linear 2 xalign 0.5
    zoom 1
    xalign 0.0
    linear 2 xalign 1.0

transform RtoL:
    linear 2 xalign 0.5
    zoom 1
    xalign 1.0
    linear 2 xalign 0.0

transform UtoD:
    linear 2 xalign 0.5
    zoom 1
    yalign 0.0
    linear 2 yalign 1.0


transform DtoU:
    xalign 0.5
    zoom 1
    yalign 1.0
    linear 2 yalign 0.0

transform DtoUxlow:
    xalign 0.5
    zoom 1
    yalign 1.0
    linear 20 yalign 0.0

transform UtoDxlow:
    xalign 0.5
    zoom 1
    yalign 0.0
    linear 20 yalign 1.0

transform DtoUlow:
    xalign 0.5
    zoom 1
    yalign 1.0
    time 1
    linear 5 yalign 0.0


transform UtoDlow:
    xalign 0.5
    zoom 1
    yalign 0.0
    time 1
    linear 5 yalign 1.0

transform updownmiddlezoom:
    zoom 1
    linear 2 xalign 0.5
    yalign 0.0
    time 1
    linear 5 yalign 1.0
    time 6
    linear 2 yalign 0.5
    time 8
    linear 2 xalign 0.6
    linear 4 zoom 2.5

transform chute:
    xalign 0.5
    zoom 1
    linear 0 yalign 1.0
    linear 2 yalign 0.2

transform sczoom:
    xalign 0.5
    zoom 0
    yalign 0.5
    ypos 1.0
    linear 2 zoom 1 ypos 0.5
