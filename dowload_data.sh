if [ -e "lfw-funneled.tgz" ]; then
    echo 'File already exists' >&2
else
    curl -o "lfw-funneled.tgz" "http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz"
fi
tar zxf lfw-funneled.tgz