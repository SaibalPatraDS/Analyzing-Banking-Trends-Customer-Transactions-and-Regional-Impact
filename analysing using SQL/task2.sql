/* Find the user who made the largest deposit amount and the transaction type for that deposit. */

--- Find the user who made the largest deposit amount and the transaction type for that deposit.

SELECT consumer_id,
       transaction_type,
       transaction_amount
FROM user_transaction
WHERE transaction_amount = (SELECT MAX(transaction_amount)
                             FROM user_transaction)
     AND transaction_type = 'deposit';
