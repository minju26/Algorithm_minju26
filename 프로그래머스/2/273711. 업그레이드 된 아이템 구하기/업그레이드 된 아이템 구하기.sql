SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO I
JOIN ITEM_TREE T ON I.ITEM_ID = T.ITEM_ID
JOIN ITEM_INFO P ON T.PARENT_ITEM_ID = P.ITEM_ID
WHERE P.RARITY = 'RARE'
ORDER BY I.ITEM_ID DESC;
