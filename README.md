# Github Action to check review comment etiquette

Github Action to enforce reviewers to follow review etiquette


## Description
This github action uses python to parse review comment, making API calls  for retrieving and editing review comments

- Scans review comments
- Edits the review comment incase reviewer didn't Follow etiquettes 
- showing caution sign ⚠️ in beginning of original comment
- With reference link fo [PR Comment Etiquette](https://github.com/HomeXLabs/reviewington/blob/main/docs/pr_etiquette.md)
document
## Example

```bash
-name: 'review comment etiquette'
 uses: HomexLabs/review-comment-etiquette-action@v1.0.2
 with: 
   GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```



## License
[MIT](https://choosealicense.com/licenses/mit/)
