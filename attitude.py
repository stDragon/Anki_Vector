#!/usr/bin/env python3

#Say "Hey Vector" and await his response
#Edit the text between the quotes on line 23 to pick your own response

import functools
import threading
import anki_vector
from anki_vector.connection import ControlPriorityLevel
from anki_vector.events import Events

wake_word_heard = False


def main():
    evt = threading.Event()

    def on_wake_word(robot, event_type, event, msg):
        robot.conn.request_control()

        global wake_word_heard
        if not wake_word_heard:
            wake_word_heard = True
            robot.behavior.say_text("I'm getting a little fed up with all these demands")
            evt.set()

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial,
                           behavior_control_level=ControlPriorityLevel.DEFAULT_PRIORITY,
                           cache_animation_lists=False) as robot:
        on_wake_word = functools.partial(on_wake_word, robot)
        robot.events.subscribe(on_wake_word, Events.wake_word)

        print('------ Vector is waiting to hear "Hey Vector!" Press ctrl+c to exit early ------')

        try:
            if not evt.wait(timeout=10):
                print('------ Vector never heard "Hey Vector!" ------')
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
