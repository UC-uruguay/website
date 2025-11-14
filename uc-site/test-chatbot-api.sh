#!/bin/bash
echo "🧪 Claude API テスト"
echo "===================="
echo ""

# Test 1
echo "質問1: どこに住んでるの？"
curl -s -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"どこに住んでるの？"}' | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('回答:', data['response'])
print()
"

# Test 2  
echo "質問2: 好きな食べ物は？（知らない質問）"
curl -s -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"好きな食べ物は？"}' | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('回答:', data['response'])
print()
"

# Test 3
echo "質問3: 何か面白い話して"
curl -s -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"何か面白い話して"}' | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('回答:', data['response'])
"
