

from pyngrok import ngrok, conf
import streamlit as st
import time                         
import os

NGROK_PORT = "8501" 
NGROK_EXE_PATH = "D:\\ngrok\\ngrok.exe"
NGROK_AUTHTOKEN_FROM_ENV= os.getenv("NGROK_AUTHTOKEN")

pyngrok_config_overrides = {
    "ngrok_path": NGROK_EXE_PATH,
    "auth_token": NGROK_AUTHTOKEN_FROM_ENV, 
    # "region": "jp"  
    }

new_config = conf.PyngrokConfig(**pyngrok_config_overrides)

print(f"NGROK_EXE_PATH used: {conf.get_default().ngrok_path}")
if conf.get_default().auth_token is not None:
    print(f"NGROK_AUTHTOKEN used (first 5 chars): {conf.get_default().auth_token[:5] if conf.get_default().auth_token else 'Not Set'}")

conf.set_default(new_config)

class Ngrok():
    @staticmethod
    def Connect():
        """
        建立连接
        """
        print("***** Ngrok.Connect() method has been CALLED! (Topmost print) *****")
        st.toast("gogogo Run Connect()", icon="🚀") 
        
        try:
            all_tunnels = ngrok.get_tunnels()
            if all_tunnels:
                for tunnel in all_tunnels:
                    if tunnel.public_url:
                        print(f"Disconnecting tunnel: {tunnel.name} ({tunnel.public_url}) forwarding to {tunnel.config['addr']}")
                        try:
                            ngrok.disconnect(tunnel.public_url)
                            print(f"Successfully disconnected {tunnel.public_url}")
                        except Exception as e:
                            print(f"Failed to disconnect {tunnel.public_url}: {e}")
                print("Finished attempting to disconnect all tunnels")
            else:
                print("No active ngrok tunnels found to disconnect")
                        
            print("Attempting to connect ngrok...")
            public_url_object = ngrok.connect(addr=NGROK_PORT, proto="http")
            public_url = public_url_object.public_url
            st.session_state.ngrok_public_url = public_url
            
        except Exception as e:
            st.session_state.ngrok_tunnel_active = False
            st.session_state.ngrok_public_url = None
            st.session_state.ngrok_error = str(e);
            print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"Error during ngrok.connect(): {e}") 
            print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return False;
        
        st.info(f"等待约 5-10 秒让应用稳定后再访问: {public_url}")
        time.sleep(10)
        return True
        
    @staticmethod
    def ShutDown():
        if st.session_state.get("ngrok_public_url"):
            try:
                ngrok.disconnect(st.session_state.ngrok_public_url)
            
            except Exception as e:
                st.session_state.ngrok_error = f"断开 ngrok 失败: {e}"
                st.sidebar.warning("断开 ngrok 时出错: {e}")
                return False
            finally:
                st.session_state.ngrok_tunnel_active = False
                st.session_state.ngrok_public_url = None
        else:
            st.session_state.ngrok_error = "没有处于活跃的ngrok!"
            return False;
        
        return True