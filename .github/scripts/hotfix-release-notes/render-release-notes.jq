# Lays out the audit's bullets as the RST lines below the component-version line.
# Input: the release-note audit. $categories: the text of the category list (categories.txt).
# Output: {"lines": [{"text": "...", "bullet": <index in .bullets, or null for a header or blank line>}],
#          "newCategories": [<headers that are not in the category list yet>]}
#
# Above 10 bullets in more than one category, the bullets are grouped under bold category headers
# (**Page Rollup**), in the order of the category list, then categories that are not listed yet,
# then Other. Bullets keep their order within a group. Otherwise the list stays flat.

def names:
  split("\n")
  | map(gsub("^[[:space:]]+|[[:space:]]+$"; ""))
  | map(select(length > 0 and (startswith("#") | not)));

($categories | names) as $list
| [.bullets | to_entries[] | {bullet: .key, text: .value.text, category: (.value.category // "Other")}] as $entries
| [$entries[].category] as $appearance
| ($appearance | unique) as $used
| if ($entries | length) > 10 and ($used | length) > 1 then
    ($used | sort_by(
      . as $category
      | ($list | index($category)) as $position
      | [
          (if $category == "Other" then 2 elif $position != null then 0 else 1 end),
          ($position // 0),
          ($appearance | index($category))
        ]
    )) as $groups
    | {
        lines: [
          $groups | to_entries[]
          | .value as $category
          | (if .key > 0 then {text: "", bullet: null} else empty end),
            {text: "**\($category)**", bullet: null},
            {text: "", bullet: null},
            ($entries[] | select(.category == $category) | {text, bullet})
        ],
        newCategories: [$groups[] | select(. as $category | $list | index($category) | not)]
      }
  else
    {lines: [$entries[] | {text, bullet}], newCategories: []}
  end
