def suggestedProducts(products, searchWord):
        products.sort()
        left,right =0,1
        outls = []

        while right < len(searchWord)+1:
            newls=[]
            for word in products:
                if word.startswith(searchWord[left:right]):
                # outls.append(word)
                    newls.append(word)
            right += 1
            ls1 = newls[:3]
            outls.append(ls1)
        return outls
suggestedProducts(["havana"], "tatiana")