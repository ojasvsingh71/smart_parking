
function reserveSlot(slotId) {
    const slot = document.getElementById(slotId);

    
    if (slot.classList.contains('reserved')) {
        alert('This slot is already reserved!');
        return;
    }

    
    document.getElementById('reservation').style.display = 'block';

    
    slot.classList.remove('available');
    slot.classList.add('reserved');

    
    slot.innerText = 'Reserved';

    
    document.getElementById('reservationForm').onsubmit = function(event) {
        event.preventDefault();

        

        alert('Reservation confirmed!');

        
        document.getElementById('reservation').style.display = 'none';
        slot.classList.remove('reserved');
        slot.classList.add('available');
        slot.innerText = 'Available';
    };
}
