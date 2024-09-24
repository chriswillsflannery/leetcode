const fs = require('fs');
const readline = require('readline');

class AppointmentScheduler {
  constructor() {
    this.providers = [];
  }

  async readInputFile(filePath) {
    const fileStream = fs.createReadStream(filePath);
    const rl = readline.createInterface({
      input: fileStream,
      crlfDelay: Infinity
    });

    let isFirstLine = true;
    for await (const line of rl) {
      if (isFirstLine) {
        isFirstLine = false;
        continue;
      }
      const [name, start, end] = line.split(',').map(item => item.trim());
      this.providers.push({ name, start, end });
    }
  }

  generateSchedule(date) {
    let output = `Appointment Schedule for ${date}\n\n`;

    for (const provider of this.providers) {
      output += `${provider.name} - Available Times:\n`;
      const availableTimes = this.calculateAvailableTimes(provider.start, provider.end);
      output += availableTimes.map(time => `  ${time}`).join('\n');
      output += '\n\n';
    }

    return output;
  }

  calculateAvailableTimes(start, end) {
    const startTime = this.parseTime(start);
    const endTime = this.parseTime(end);
    const availableTimes = [];

    let currentTime = new Date(startTime);
    currentTime.setMinutes(currentTime.getMinutes() + 5); // Add initial 5-minute buffer

    while (currentTime <= endTime) {
      const appointmentEnd = new Date(currentTime);
      appointmentEnd.setMinutes(appointmentEnd.getMinutes() + 30);

      if (appointmentEnd <= endTime) {
        availableTimes.push(this.formatTime(currentTime) + ' - ' + this.formatTime(appointmentEnd));
      }

      currentTime = new Date(appointmentEnd);
      currentTime.setMinutes(currentTime.getMinutes() + 10); // Add 10-minute buffer (5 min after previous + 5 min before next)
    }

    return availableTimes;
  }

  parseTime(timeString) {
    const [hours, minutes] = timeString.split(':').map(Number);
    const date = new Date();
    date.setHours(hours, minutes, 0, 0);
    return date;
  }

  formatTime(date) {
    return date.toTimeString().slice(0, 5);
  }
}

async function main() {
  const scheduler = new AppointmentScheduler();
  await scheduler.readInputFile('test.txt');
  const schedule = scheduler.generateSchedule('Tuesday 06/25/2024');
  console.log(schedule);
}

main().catch(console.error);