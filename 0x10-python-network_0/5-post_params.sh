#!/bin/bash
#Post a new data
curl -s -X POST -H "Content-Type: application/json" -d '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}' $@


