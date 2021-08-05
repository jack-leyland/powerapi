# Copyright (c) 2018, INRIA
# Copyright (c) 2018, University of Lille
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.

# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.

# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from enum import Enum

from powerapi.report import Report

class State(Enum):
    INIT = 1
    BLOCKED_INTER_1 = 2
    BLOCKED_INTER_2 = 3
    BLOCKED = 4
    FINAL = 5


class BlockingDetector:
    """
    Service defined for each formula that detect if the formula is blocked or not.
    A formula is defined as blocked if a three message sequence raise an exception when they are received by the formula.
    """
    def __init__(self):
        self.state = State.INIT
        self.last_poison_message_id = None
        self.max_id_value = 10000
        self.last_message_id = 0

    def notify_poison_received(self, message: Report):
        if self.state == State.INIT:
            self.state = State.BLOCKED_INTER_1
        elif message.dispatcher_report_id == self.last_poison_message_id + 1:
            if self.state == State.BLOCKED_INTER_1:
                self.state = State.BLOCKED_INTER_2
            elif self.state == State.BLOCKED_INTER_2:
                self.state = State.BLOCKED
            elif self.state == State.BLOCKED:
                self.state = State.FINAL
        elif self.state != State.BLOCKED and self.state != State.FINAL:
            self.state = State.BLOCKED_INTER_1


        if message.dispatcher_report_id == self.max_id_value:
            self.last_poison_message_id = -1
        else:
            self.last_poison_message_id = message.dispatcher_report_id 

    def is_blocked(self) -> bool:
        return self.state == State.BLOCKED

    def get_message_id(self):
        message_id = self.last_message_id
        if self.last_message_id == self.max_id_value:
            self.last_message_id = 0
        else:
            self.last_message_id += 1
        return message_id
    
