# Github Action to check review comment etiquette

Github Action to enforce reviewers to follow review etiquette


## Description
This github action uses python to parse review comment, making API calls  for retrieving and editing review comments

- Scans review comments
- Edits the review comment incase reviewer didn't Follow etiquettes 
- showing caution sign ⚠️ at beginning of original comment
- With reference link fo [PR Comment Etiquette](https://github.com/HomeXLabs/reviewington/blob/main/docs/pr_etiquette.md)
document
## Example

```bash
name: Reviewington 
on:
  pull_request_review_comment:
    types: [created, edited]
jobs:
  reviewington:
    name: reviewington check
    runs-on: ubuntu-latest
    steps:
      - name: review-comment-etiquette
        uses: HomeXLabs/review-comment-etiquette-action@v1.0.1
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```



## License
[MIT](https://choosealicense.com/licenses/mit/)
