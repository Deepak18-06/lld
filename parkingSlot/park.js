class ParkingLot {
    constructor(capacity) {
        this.capacity = capacity;
        this.availableSlots = new Array(capacity).fill(true); // true indicates slot is available, false indicates slot is occupied
        this.occupiedSlots = {}; // Map to store vehicle information occupying each slot
    }

    park(vehicleNumber) {
        const slotNumber = this.availableSlots.findIndex(slot => slot === true); // Find the first available slot
        if (slotNumber === -1) {
            console.log("Parking lot is full");
            return;
        }
        this.availableSlots[slotNumber] = false; // Mark slot as occupied
        this.occupiedSlots[slotNumber] = vehicleNumber; // Store vehicle information
        console.log(`Vehicle with number ${vehicleNumber} parked at slot ${slotNumber}`);
    }

    unpark(slotNumber) {
        if (!this.availableSlots[slotNumber]) {
            delete this.occupiedSlots[slotNumber]; // Remove vehicle information from occupiedSlots map
            this.availableSlots[slotNumber] = true; // Mark slot as available
            console.log(`Vehicle parked at slot ${slotNumber} has been unparked`);
        } else {
            console.log(`Slot ${slotNumber} is already empty`);
        }
    }

    getStatus() {
        console.log("Parking Lot Status:");
        for (let i = 0; i < this.capacity; i++) {
            if (this.availableSlots[i]) {
                console.log(`Slot ${i}: Empty`);
            } else {
                console.log(`Slot ${i}: Occupied by Vehicle Number ${this.occupiedSlots[i]}`);
            }
        }
    }
}

// Example usage:
// const parkingLot = new ParkingLot(5); // Create a parking lot with capacity of 5 slots
// parkingLot.park("ABC123"); // Park a vehicle with number "ABC123"
// parkingLot.park("XYZ456"); // Park another vehicle with number "XYZ456"
// parkingLot.getStatus(); // Print the status of the parking lot
// parkingLot.unpark(0); // Unpark the vehicle at slot 0
// parkingLot.getStatus(); // Print the status of the parking lot after unparking


function fetchData() {
    return new Promise((resolve, reject) => {
        // Simulating an asynchronous operation (e.g., fetching data from a server)
        setTimeout(() => {
            const data = { name: 'John', age: 30 };
            resolve(data); // Resolve the promise with some data
            // If there's an error, you can reject the promise with an error message:
            // reject('Error fetching data');
        }, 1000);
    });
}

async function fetchDataAsync() {
    try {
        console.log("heyy")
        const data = await fetchData(); // Wait for the promise to be resolved
        console.log(data); // Output: { name: 'John', age: 30 }
        console.log("hey")
    } catch (error) {
        console.log(error);
    }
}

fetchDataAsync();
