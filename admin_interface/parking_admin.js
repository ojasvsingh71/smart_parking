
function toggleSlot(slotId) {
    const slot = document.getElementById(slotId);

    
    if (slot.classList.contains('available')) {
        slot.classList.remove('available');
        slot.classList.add('occupied');
    } else if (slot.classList.contains('occupied')) {
        slot.classList.remove('occupied');
        slot.classList.add('available');
    }

    
    updateSummary();
}


function updateSummary() {
    const availableSlots = document.querySelectorAll('.slot.available').length;
    const occupiedSlots = document.querySelectorAll('.slot.occupied').length;

    document.getElementById('availableSlots').textContent = `Available Slots: ${availableSlots}`;
    document.getElementById('occupiedSlots').textContent = `Occupied Slots: ${occupiedSlots}`;
}
