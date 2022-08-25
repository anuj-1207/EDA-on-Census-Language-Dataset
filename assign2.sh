#!/bin/bash
start=$SECONDS

sh percent-india.sh
sh gender-india.sh
sh geography-india.sh
sh 3-to-2-ratio.sh
sh 2-to-1-ratio.sh
sh age-india.sh
sh literacy-india.sh
sh region-india.sh
sh age-gender.sh
sh literacy-gender.sh

end=$SECONDS

echo "duration: $((end-start)) seconds."
