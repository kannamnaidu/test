#!/bin/bash
# set -e
# set -eo pipefail
echo $PROJECT_ID

declare -a dir_list=(
[0]=BASE_TABLE
[1]=VIEW
[2]=FUNCTION
[3]=PROCEDURE
[4]=CUSTOM_DML
)

# here we get parents of latest commit (parents of merge request)
PARENTS_COMMIT_HASH=$(git log --pretty=%P -n 1 $(git rev-parse --short HEAD))

# below command is used to get list of files difference from current merge request to last merge request
for parent_commit in ${PARENTS_COMMIT_HASH}
do
    LATEST_FILES=$(git diff --name-only $(git rev-parse --short HEAD) $parent_commit)
    echo "List of files needs to be deploy:- ${LATEST_FILES}"
    break
done

for a in ${dir_list[@]}
do
    echo "In Directory---$a"
    for file in ${LATEST_FILES}
    do
        # Here check file is from above list of folders only
        if [[ $file == *"$a"* ]]; then
            # Here check file exist or not
            if [[ -e $file ]]; then
                # Here we split file name
                arr=(${file//"/"/ })
                # Flag is set to display error and continue process of deployment
                set -e
                /usr/bin/python3 bq.py ${arr[0]}/${arr[1]} | echo
            fi 
        fi
    done
done
