[[ ! -f eu.json ]] && curl https://usegalaxy.eu/api/tools?in_panel=false > eu.json
[[ ! -f us.json ]] && curl https://usegalaxy.org/api/tools?in_panel=false > us.json
[[ ! -f au.json ]] && curl https://usegalaxy.org.au/api/tools?in_panel=false > au.json
[[ ! -f fr.json ]] && curl https://usegalaxy.fr/api/tools?in_panel=false > fr.json
[[ ! -f be.json ]] && curl https://usegalaxy.be/api/tools?in_panel=false > be.json
