meetings_list = [
    ["Monday", "3:30 PM", "Joe", "Sam"],
    ["Monday", "4:30 PM", "Bob", "Alice"],
    ["Tuesday", "3:30PM", "Joe", "Bob", "Alice", "Sam"],
    ["Tuesday", "9:30 AM", "Joe", "Bob"],
]

participants = input()
meeting_participate = ""

for meeting in meetings_list:
    if participants in meeting:
        meeting_participate += f"{participants} to participate in the meeting : {meeting[0]} at {meeting[1]}\n"
print(meeting_participate)
