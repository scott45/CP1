from room import Room


class LivingSpace(Room):
    """
    The Office class is also a sub-class of the 'Room'
    class meaning it inherits 'room_name'.
    """
    roomCapacity = 4




room = LivingSpace()
room.create_room('o', 'krew', 'ewwe', 'reew')
print(room.all_rooms)

