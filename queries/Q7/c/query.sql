select count(*) as total_rows from (

select tconst, count(nconst)
           from `title.principals`
           where category = 'actress'
group by tconst
having count(nconst) >= 4

) a