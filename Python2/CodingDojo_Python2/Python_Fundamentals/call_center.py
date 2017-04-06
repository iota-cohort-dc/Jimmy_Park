# call center


class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def display_all(self):
        print [self.unique_id, self.caller_name, self.caller_phone_number, self.time_of_call, self.reason_for_call]

class CallCenter(Call):
    def __init__(self):
        super(CallCenter, self).__init__(self, calls, queue_size)
        self.call = [self.unique_id, self.caller_name, self.caller_phone_number, self.time_of_call, self.reason_for_call]
        self.queue_size = len(call)
    def display_all_calls(self):
        print [self.calls, self.queue_size]




CallFromJim = Call(416, "jimmy", "781-571-9437", 515, "to get the assignments")


CallFromJim.display_all()
# this returns: [416, 'jimmy', '781-571-9437', 515, 'to get the assignments']
CallFromJim.display_all_calls()
