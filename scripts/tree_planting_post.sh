#!/bin/bash

USERNAME="uc-japan"
APP_PASSWORD="MWExSgYfvQ98OmvvJ7rfuibb"

# Japanese post
curl -X POST "https://uc.x0.com/wp-json/wp/v2/posts" \
  -u "${USERNAME}:${APP_PASSWORD}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "ソーシャルテンプルの植樹イベントに参加",
    "content": "<p>昨日、ソーシャルテンプルの植樹イベントに参加してきました。55人もの参加者で、660本くらいの木の苗を植えました。23種類くらい植えました。</p><p>これは、自然淘汰の末に、種類はだんだん減って、その土地に適した森を作るためだと言います。1種類だと、病気がすぐに蔓延してしまったり、火が起きたときに広がりやすい性質があると言い、それらを防ぐ効果もあるそうです。</p><p>植樹が終わった後は飲み会。色々縁がある人がいました。中でもびっくりしたのは、出身地が一緒というので話していると、私の高校の先生をしていた人とも出会えたことです。時期は被っていなかったので、初見でしたが、素晴らしい出会いとなりました。</p><p>地球に良い事をして、後世に良い環境を残していきたいです。</p>",
    "status": "publish",
    "categories": [1]
  }'

echo -e "\n\n=== Creating English version ===\n"

# English post
curl -X POST "https://uc.x0.com/wp-json/wp/v2/posts" \
  -u "${USERNAME}:${APP_PASSWORD}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Participated in Social Temple Tree Planting Event",
    "content": "<p>Yesterday, I participated in the Social Temple tree planting event. With 55 participants, we planted around 660 tree saplings of approximately 23 different species.</p><p>This diversity is intentional - through natural selection, the number of species will gradually decrease, allowing the forest to adapt to the local environment. Planting only one species makes the forest vulnerable to disease spread and increases fire risk, so this biodiversity approach helps prevent these issues.</p><p>After the tree planting, we had a social gathering. I met many people with interesting connections. What surprised me most was discovering that one person had taught at my high school! Although our times there didn'\''t overlap, it was a wonderful encounter.</p><p>I want to continue doing good things for the Earth and leaving a better environment for future generations.</p>",
    "status": "publish",
    "categories": [1]
  }'
