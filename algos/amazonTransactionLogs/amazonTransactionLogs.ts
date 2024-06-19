/*

Amazon transaction logs
Your team is responsible for maintaining a monetary transaction service. The transactions are
tracked in a log file.
A log file is provided as a string array where each entry represents a transaction to service.
Each transaction consists of:
- sender_user_id: UUI for the user that initiated the transaction. At most 9 digits.
- recipient_user_id: user receiving transaction. at most 9 digits
- amount_of_transaction: at most 9 digits

The values are separated by a space. For example, "sender_user recipient_user amount"
Users that perform an excessive amount of transactions might be abusing the service so you have been
tasked to identify the users that have a number of transactions over a threshold.  The list of user
ids should be ordered in ascending numeric value.

Example logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
id  transactions
99  3
88  2
12  1
32  1

Note: in the last log entry, 12 is both sender and receiver. This only counts as one transaction.

There are 2 users who meet the threshold of 2. Return: ['88', '99'] (ascending order)

*/

function processLogs(logs: string[], threshold) {
  // Write your code here
  // split logs on each entry for 0 = sender, 1 = receiver, 2 = amount
  // for each set of entries
  // if sender and receiver same, include as single entry in hash
  // else increment hash for sender and receiver accordingly

  // [["88", "99", "200"], ...]
  const splitlog = logs.map((log) => log.split(" "));

  const hash: Record<string, number> = {};
  for (let entry of splitlog) {
    const sender = entry[0];
    const rec = entry[1];

    if (sender !== rec) {
      hash[rec] ? (hash[rec] += 1) : (hash[rec] = 1);
    }
    hash[sender] ? (hash[sender] += 1) : (hash[sender] = 1);
  }

  // [[88, 2], [99, 3]]
  const sortedAscending = Object.entries(hash).sort((a, b) => {
    if (a[1] > b[1]) {
      return 1;
    } else {
      return -1;
    }
  });

  return sortedAscending
    .filter((entry) => entry[1] >= threshold)
    .map((entry) => entry[0]);
}
