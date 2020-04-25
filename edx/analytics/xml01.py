from  lxml import etree
import os

cur_dir=os.getcwd()
fichero=cur_dir + '\\prueba.xml'
datos="""<Catalog> 
   <Book id='bk101'> 
      <Author>Garghentini, Davide</Author>
      <Title>XML Developers Guide</Title>
      <Genre>Computer</Genre>
      <Price>44.95</Price>
      <PublishDate>2000-10-01</PublishDate>\
      <Description>An in-depth look at creating applications
      with XML.</Description>
   </Book>
   <Book id='bk102'>
      <Author>Garcia, Debra</Author>
      <Title>Midnight Rain</Title>
      <Genre>Fantasy</Genre>
      <Price>5.95</Price>
      <PublishDate>2000-12-16</PublishDate>\
      <Description>A former architect battles corporate zombies,
      an evil sorceress, and her own childhood to become queen
      of the world.</Description>
   </Book>
</Catalog>"""
root=etree.XML(datos)
#root=etree.parse(fichero)
print(root.tag)
print(etree.tostring(root,pretty_print=True).decode())