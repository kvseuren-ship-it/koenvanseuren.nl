from PIL import Image, ImageOps
import os
R='/home/claude/raw'
M={
 'vvv-1':'ak/vvv__VVV6.png',
 'zelfmoordenaar-1':'ak/zelfmoordenaar__NL_De-Zelfmoordenaar-16x9-autoxauto-klein.jpg',
 'wzna-1':'ig/ig-09-Da2iz6.jpg','wzna-2':'ig/ig-11-Da2iz6.jpg','wzna-3':'ig/ig-10-Da2iz6.jpg','wzna-4':'ig/ig-01-x.jpg','wzna-5':'ig/ig-02-x.jpg',
 'herzschmerz-1':'ak/herzschmerz__Herzschmerz---Antiklimax-NielsKnelis-0202-DSC_4236.jpg',
 'herzschmerz-2':'ak/herzschmerz__Herzschmerz---Antiklimax-NielsKnelis-0043-B0005297.jpg',
 'herzschmerz-3':'ak/herzschmerz__Herzschmerz---Antiklimax-NielsKnelis-0093-B0005458.jpg',
 'herzschmerz-4':'ak/herzschmerz__Herzschmerz---Antiklimax-NielsKnelis-0062-DSC_1953.jpg',
 'herzschmerz-5':'ak/herzschmerz__Herzschmerz---Antiklimax-NielsKnelis-0035-B0005231.jpg',
 'herzschmerz-6':'ak/herzschmerz__Herzschmerz---Antiklimax-NielsKnelis-0127-DSC_2952.jpg',
 'revenge-1':('ig/ig-15-HZT-Revenge.jpg',0.70),'revenge-2':('ig/ig-17-HZT-Revenge.jpg',0.64),'revenge-3':'ig/ig-18-HZT-RevengeCampaign.jpg',
 'atwh-1':'ak/atwh__1500.jpg','atwh-2':'grand/g07_antiklimax-astheworldhurts-nielsknelis-0005-dsc_0248.jpg','atwh-3':'grand/g08_antiklimax-astheworldhurts-nielsknelis-0013-dsc_9404.jpg',
 'hamlet-1':'ak/hamlet__Hamlet-2400.jpg','hamlet-2':'ak/hamlet__DONvsHAM-Antiklimax-Nielsknelis-DEF-0008-DSC_3405.jpg','hamlet-3':'ak/hamlet__DONvsHAM-Antiklimax-Nielsknelis-DEF-0011-DSC_3699.jpg','hamlet-4':'grand/g12_donvsham_antiklimax_nielsknelis-0175-dsc_4054.jpg',
 'peergynt-1':'ak/peergynt__Peer-Gynt-2400.jpg','peergynt-2':'ak/peergynt__NielsKnelis-Antiklimax-2juni-143-DSC_5536.jpg','peergynt-3':'ak/peergynt__NielsKnelis-Antiklimax-2juni-049-DSC_1951.jpg','peergynt-4':'ak/peergynt__NielsKnelis-Antiklimax-2juni-082-DSC_5372.jpg',
 'portret':'ig/ig-12-HZT-DLzsEj.jpg',
}

M.update({
 'poster-peergynt':'grand/g13_peer-gynt.jpg','poster-hamlet':'grand/g10_nielsknelis-antiklimax-0439-_dsc4222.jpg','poster-atwh':'grand/g09_antiklimax-2023-nielsknelis-0038-dsc_2014.jpg',
 'poster-herzschmerz':'grand/g01_antiklimax_herzschmerz-nielsknelis-2.jpg','poster-funf':'grand/g15_funf.jpg','poster-revenge':'grand/g16_revenge.jpg','herzschmerz-11':'grand/g02_herzschmerz-antiklimax-nielsknelis-0113-dsc_2586.jpg','herzschmerz-12':'grand/g04_herzschmerz-beeld-liggend-1.png','atwh-11':'grand/g05_antiklimax-astheworldhurts-nielsknelis-0009-dsc_9096.jpg','atwh-12':'grand/g06_antiklimax-astheworldhurts-nielsknelis-0015-dsc_0899.jpg','poster-zelfmoordenaar':'akig/ak-02.jpg',
 'herzschmerz-7':'akig/ak-05.jpg','herzschmerz-8':'akig/ak-09.jpg',
 'atwh-4':'akig/ak-39.jpg','atwh-5':'akig/ak-40.jpg','atwh-6':'akig/ak-41.jpg','atwh-7':'akig/ak-43.jpg','atwh-8':'akig/ak-46.jpg','atwh-10':'akig/ak-45.jpg',
 'hamlet-6':'akig/ak-59.jpg','hamlet-7':'akig/ak-65.jpg',
 'peergynt-6':'akig/ak-70.jpg','peergynt-7':'akig/ak-74.jpg',
 'zelfmoordenaar-2':'akig/ak-00.jpg',
 'makers':'akig/ak-01.jpg','makers-2':'akig/ak-76.jpg',
})

def run(out, only=None):
    os.makedirs(out,exist_ok=True); dims={}
    for k,v in M.items():
        if only and k not in only: continue
        crop=None
        if isinstance(v,tuple): v,crop=v
        im=Image.open(os.path.join(R,v)); im=ImageOps.exif_transpose(im).convert('RGB')
        if crop: im=im.crop((0,0,im.width,int(im.height*crop)))
        for suf,mx,q in (('',1600,80),('-sm',760,76)):
            t=im.copy(); t.thumbnail((mx,mx),Image.LANCZOS)
            t.save(f'{out}/{k}{suf}.jpg','JPEG',quality=q,optimize=True,progressive=True)
        t=im.copy(); t.thumbnail((1600,1600)); dims[k]=t.size
    return dims
if __name__=='__main__':
    import sys; d=run(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','site','img'), only=set(sys.argv[1:]) or None); print(d)
