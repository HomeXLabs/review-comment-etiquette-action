# review-comment-etiquette-action
Github action to check review comment etiquette

It scan review comments and edit the review comment if etiqutte is not followed
⚠️ showing caution sign in begining and refrence link for etiquette
⚠️ PR Comment Etiquette not followed on above comment ⚠️

Input required : GITHUB_TOKEN \n
\n
example: \n
    -name: 'review comment etiquette' \n
     uses: HomexLabs/review-comment-etiquette-action@v1 \n
     with: \n
       GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} \ n
