#!/bin/bash

# WordPress API configuration
WORDPRESS_URL="https://uc.x0.com"
JWT_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VjLngwLmNvbSIsImlhdCI6MTc1NjgxMDIzNiwiZXhwIjoxNzU2ODEzODM2LCJ1c2VyX2lkIjoxLCJqdGkiOiJCQ08yTTluM2tnN2FNbHRaN2p1N1J6M09pSWl5RXBBayJ9.F89PaKJxhGRzcO4KBjI7GfnEPQ5F0OCEUICX1l__-hY"

# Create the post content in HTML format
POST_CONTENT='
<h2>Meeting Minutes: Self-Sufficient Village Concept Meeting</h2>

<p><strong>Date:</strong> September 25, 2025<br>
<strong>Participants:</strong> Mr. Sugihara, UC<br>
<strong>Agenda:</strong> Self-sufficient village concept and idea brainstorming</p>

<h3>1. Village Concept: "Modern Self-Sufficient Utopia"</h3>
<p>Our goal is not just self-sufficiency, but a community filled with richness and joy.</p>

<h4>Core Philosophy:</h4>
<ul>
<li>Modernize traditional living (like "From the Northern Country" TV series) with contemporary knowledge (YouTube etc.) and tools for efficiency</li>
<li>Use time gained through efficiency for "play" and creative activities</li>
</ul>

<h4>Economic Independence:</h4>
<ul>
<li>Not a closed community - build a model to earn external income by sharing village-building activities on social media</li>
<li>Establish a "Village Fund" with abundant resources to support villagers'\'' dreams (overseas travel, entrepreneurship, etc.)</li>
</ul>

<h4>Vision:</h4>
<p>Aim for a "utopia" where everything needed for life, opportunities for challenges, and companions are all available.</p>

<h3>2. Village Economic System</h3>
<p>Lively discussions were held on how to circulate the economy within the community.</p>

<h4>Internal Economy (among villagers):</h4>
<p><strong>Sugihara's proposal - Community currency with expiration dates:</strong><br>
Introduce a system like eumo to activate economic circulation within the village.</p>

<p><strong>UC's proposal - Bartering system:</strong><br>
Make bartering the foundation since currency can create ulterior motives. This creates negotiation enjoyment and fosters a community that requires honesty.</p>

<p><strong>Idea - Handmade currency:</strong><br>
Analog, warm currency where we write expiration dates on paper and stamp with thumbprints could be interesting.</p>

<h4>External Economy (tourists and external exchanges):</h4>
<ul>
<li>Consider issuing pseudo-currency as incentives for tourists</li>
<li>Consider introducing eumo etc. for external payments. Limited participating stores create value of "seeing producers'\'' faces"</li>
</ul>

<h3>3. Village Management System and Infrastructure</h3>
<p>Building sustainable and scalable systems.</p>

<h4>Systemization and Horizontal Expansion:</h4>
<ul>
<li>Package management systems to create sister villages in the future (goal: 48 villages!)</li>
<li>Set up "Village Registry" and "Occupation Introduction Pages" on village website with auto-updating form input systems for easy implementation in other villages</li>
<li>As villages increase, a culture like "pilgrimage" visiting village to village might emerge</li>
</ul>

<h4>Infrastructure (achieving self-sufficiency):</h4>
<p><strong>Energy:</strong> Firewood for thermal power, utilize discarded items for electricity. Solar heat with parabolic antenna systems for hot water.</p>

<p><strong>Resources:</strong> Reuse waste materials for toilets and renovation materials. Actively upcycle by disassembling EcoCute units to create homemade stainless tanks.</p>

<h3>4. Villagers'\'' Life and Participation Conditions</h3>
<p>Creating systems for villagers to live safely and authentically.</p>

<h4>Work Style:</h4>
<p>Promote flexible styles where various jobs can be held simultaneously within legal boundaries.</p>

<h4>Village Tax (proposal):</h4>
<p>Register for basic income like OpenAI's Worldcoin, and use that income as "village tax." This eliminates actual financial burden on villagers.</p>

<h4>Safety Net:</h4>
<p>Being a villager provides insurance-like function to evacuate to the village during disasters.</p>

<h4>Village Entry Screening:</h4>
<p>Emphasize shared values with careful screening process:</p>
<ul>
<li>Interviews</li>
<li>Recommendation letters from 3 trusted friends</li>
<li>Friends accompanying interviews</li>
</ul>

<h3>5. Future Prospects</h3>
<p>Grand plans were shared as the village's future vision:</p>
<ul>
<li>Expand sister villages nationwide</li>
<li>Eventually collaborate/integrate (take over) municipalities at risk of disappearing to establish genuine self-sufficient villages</li>
<li>Purchasing uninhabited islands (Setouchi islands accessible by boat) is also attractive</li>
</ul>

<hr>

<p><em>This meeting laid the foundation for an innovative approach to modern community living, combining traditional self-sufficiency with contemporary technology and social systems.</em></p>
'

# Create the API request
curl -X POST "${WORDPRESS_URL}/wp-json/wp/v2/posts" \
     -H "Authorization: Bearer ${JWT_TOKEN}" \
     -H "Content-Type: application/json" \
     -d "{
       \"title\": \"Meeting Minutes: Self-Sufficient Village Concept - Modern Utopia Vision\",
       \"content\": \"${POST_CONTENT}\",
       \"status\": \"publish\",
       \"categories\": [1],
       \"tags\": []
     }"

echo "Self-Sufficient Village Meeting Minutes post has been published!"