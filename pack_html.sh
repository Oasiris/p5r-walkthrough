mkdir dist/
python3 bin/coop-answers.py
python3 bin/full-walkthroughs.py
python3 bin/html-walkthrough.py $1
cp src/style/**.css dist
echo "Packed! View by running 'npm run start'"